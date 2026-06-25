import pytest
import sys
sys.path.insert(0, './src')
from codefree_builder import Config, generate_code, validate_code, generate_type_annotations, add_error_handling

def test_generate_code():
    config = Config(components=["header", "footer"], layout="main")
    code = generate_code(config)
    assert "header" in code
    assert "footer" in code
    assert "main" in code

def test_validate_code():
    code = "import * as React from 'react';\n\nconst App: React.FC = () => {\n return <div>main</div>;\n};\n\nexport default App;\n"
    assert validate_code(code)

def test_generate_type_annotations():
    code = "const App: React.FC = () => {\n return <div>main</div>;\n};\n\nexport default App;\n"
    annotated_code = generate_type_annotations(code)
    assert "// type: any" in annotated_code

def test_add_error_handling():
    code = "const App: React.FC = () => {\n return <div>main</div>;\n};\n\nexport default App;\n"
    handled_code = add_error_handling(code)
    assert "try {" in handled_code
    assert "catch (error) {" in handled_code
