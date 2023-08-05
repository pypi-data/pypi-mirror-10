import avro.schema
import os
import json
import validate
import copy
import yaml
import copy
import logging
import pprint
from aslist import aslist
import avro_ld.schema

TOOL_CONTEXT_URL = "https://raw.githubusercontent.com/common-workflow-language/common-workflow-language/master/schemas/draft-2/cwl-context.json"
module_dir = os.path.dirname(os.path.abspath(__file__))

_logger = logging.getLogger("cwltool")

class WorkflowException(Exception):
    pass

def get_schema():
    cwl_avsc = os.path.join(module_dir, 'schemas/draft-2/cwl-avro.yml')
    with open(cwl_avsc) as f:
        j = yaml.load(f)
        return avro_ld.schema.schema(j)

class Process(object):
    def check_feature(self, feature, kwargs):
        for t in kwargs.get("requirements", []):
            if t["class"] == feature:
                return True
        for t in kwargs.get("hints", []):
            if t["class"] == feature:
                return True
        return False

    def __init__(self, toolpath_object, validateAs, docpath):
        self.names = get_schema()
        self.docpath = docpath

        self.tool = toolpath_object

        #if self.tool.get("@context") != TOOL_CONTEXT_URL:
        #    raise Exception("Missing or invalid '@context' field in tool description document, must be %s" % TOOL_CONTEXT_URL)

        # Validate tool documument
        validate.validate_ex(self.names.get_name(validateAs, ""), self.tool)

        self.validate_requirements(self.tool, "requirements")
        self.validate_requirements(self.tool, "hints")

        for t in self.tool.get("requirements", []):
            t["_docpath"] = docpath

        for t in self.tool.get("hints", []):
            t["_docpath"] = docpath

        # Import schema defs
        self.schemaDefs = {
            "Any": [
                "null",
                "boolean",
                "int",
                "long",
                "float",
                "double",
                "bytes",
                "string",
                "File",
                {"type": "array", "items": "Any"},
                {"type": "map", "values": "Any"}
            ]}

        if self.tool.get("schemaDefs"):
            for i in self.tool["schemaDefs"]:
                avro.schema.make_avsc_object(i, self.names)
                self.schemaDefs[i["name"]] = i

        # Build record schema from inputs
        self.inputs_record_schema = {"name": "input_record_schema", "type": "record", "fields": []}
        for i in self.tool["inputs"]:
            c = copy.copy(i)
            c["name"] = c["id"][1:]
            del c["id"]
            if "default" in c:
                c["type"] = ["null"] + aslist(c["type"])
            self.inputs_record_schema["fields"].append(c)
        avro.schema.make_avsc_object(self.inputs_record_schema, self.names)

        self.outputs_record_schema = {"name": "outputs_record_schema", "type": "record", "fields": []}
        for i in self.tool["outputs"]:
            c = copy.copy(i)
            c["name"] = c["id"][1:]
            del c["id"]
            if "default" in c:
                c["type"] = ["null"] + aslist(c["type"])
            self.outputs_record_schema["fields"].append(c)
        avro.schema.make_avsc_object(self.outputs_record_schema, self.names)

    def validate_requirements(self, tool, field):
        for r in tool.get(field, []):
            try:
                if self.names.get_name(r["class"], "") is None:
                    raise validate.ValidationException("Unknown requirement %s" % (r["class"]))
                validate.validate_ex(self.names.get_name(r["class"], ""), r)
                if "requirements" in r:
                    self.validate_requirements(r, "requirements")
                if "hints" in r:
                    self.validate_requirements(r, "hints")
            except validate.ValidationException as v:
                err = "While validating %s %s\n%s" % (field, r["class"], validate.indent(str(v)))
                if field == "hints":
                    _logger.warn(err)
                else:
                    raise validate.ValidationException(err)
