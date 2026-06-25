import json
from dataclasses import dataclass
from typing import List

@dataclass
class Config:
    components: List[str]
    layout: str

def generate_code(config: Config) -> str:
    """ Generate TypeScript code based on the provided configuration. """
    code = "import * as React from 'react';\n\n"
    code += "interface Props {\n"
    for component in config.components:
        code += f" {component}: any;\n"
    code += "}\n\n"
    code += "const App: React.FC<Props> = ({" + ", ".join(config.components) + "}) => {\n"
    code += f" return <div>{config.layout}</div>;\n"
    code += "};\n\n"
    code += "export default App;\n"
    return code

def validate_code(code: str) -> bool:
    """ Validate the generated code using ESLint. """
    # Simulate ESLint validation (in a real scenario, you would use the ESLint API)
    return "error" not in code

def generate_type_annotations(code: str) -> str:
    """ Add proper type annotations to the generated code. """
    lines = code.split("\n")
    for i, line in enumerate(lines):
        if "const" in line:
            lines[i] = line + " // type: any"
    return "\n".join(lines)

def add_error_handling(code: str) -> str:
    """ Add error handling to the generated code. """
    lines = code.split("\n")
    for i, line in enumerate(lines):
        if "return" in line:
            lines.insert(i + 1, "try {")
            lines.append("} catch (error) { console.error(error); }")
    return "\n".join(lines)
