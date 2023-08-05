from pathlib import Path
import ml_project_template
import argparse

def main():

    parser = argparse.ArgumentParser(prog ='mlproject',
                                     description ='Create ML Project Template')
  
    parser.add_argument('project_path', metavar='project_path', action ='store',
                        default = False, help ="Root path for the project.")
    parser.add_argument('--package_name', '-n', dest ='package_name', action ='store',
                        default = 'ml_project',
                        help ='Name of the package to be created.')
  
    args = parser.parse_args()

    root_path = Path(ml_project_template.__file__).resolve().parent / 'files'
    print(root_path)

    print("Hello")

    output_path_root = Path(args.project_path).resolve()
    package_name = args.package_name

    print(f"Creating the template in {output_path_root}")

    output_path_root.mkdir()

    for path in sorted(root_path.rglob('*')):
        first_dir = path.relative_to(root_path).parts [0]
        if first_dir == '.git' or first_dir == '.ipynb_checkpoints' or path.suffix == '.sh' or "__pycache__" in path.relative_to(root_path).parts:
            continue
        if path.is_dir():
            output_path_dir = output_path_root/ Path(*[p if p!='recoform' else package_name for p in path.relative_to(root_path).parts])
            print(output_path_dir)
            output_path_dir.mkdir()
            continue
        print(path.relative_to(root_path))
        text = path.read_text()
        # print(text)
        text = text.replace('recoform', package_name)
        
        output_path = output_path_root / Path(*[p if p!='recoform' else package_name for p in path.relative_to(root_path).parts])
        output_path.write_text(text)