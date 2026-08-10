from client import MultimodalVisionDocumentFlowchartParserClient

def main():
    client = MultimodalVisionDocumentFlowchartParserClient()
    res = client.parse_flowchart("architecture_diagram.png", "MERMAID")
    print(f"Nodes Extracted: {res['nodes_count']}")
    print(f"Confidence: {res['parsing_confidence']}")
    print("Parsed Mermaid Syntax:")
    print(res["parsed_mermaid_syntax"])

if __name__ == "__main__":
    main()
