import os
import argparse
from tree_sitter import Language, Parser
import csv

def main(code_path, output_file):
    # Set up parsers
    matlab_lang = Language('path/to/tree-sitter-matlab.wasm', 'matlab')
    stata_lang = Language('path/to/tree-sitter-stata.wasm', 'stata')
    
    results = []
    
    # Walk files & parse
    for root, dirs, files in os.walk(code_path):
        for file in files:
            file_path = os.path.join(root, file)
            
            if file.endswith('.m'):
                lang = matlab_lang 
            elif file.endswith(('.do', '.ado')):
                lang = stata_lang
            else:
                continue
                
            with open(file_path) as f:
                code = f.read()
                
            parser = Parser()
            tree = parser.parse(code, lang)
            
            lines = len(code.split('\n'))
            complexity = compute_complexity(tree.root_node)
            
            results.append([file_path, lang.name, lines, complexity])
            
     # Write results         
    with open(output_file, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['file_path', 'language', 'lines', 'complexity']) 
        writer.writerows(results)
        
if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description='Compute code complexity metrics'
    )
    parser.add_argument('codepath', help='Root path of codebase')  
    parser.add_argument('-o', '--outdir', required=True,  
                        help='Output directory for metrics file')
    parser.add_argument('-f', '--outfile', required=True,
                        help='Filename for metrics CSV output')
    args = parser.parse_args()

    output_file = os.path.join(args.outdir, args.outfile)


if __name__ == '__main__':
    main(args.codepath, output_file)