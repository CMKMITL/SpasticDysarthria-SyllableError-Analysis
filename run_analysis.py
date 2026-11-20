"""Run the manuscript notebook code in order without opening Jupyter."""

import argparse
import os
import json
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--skip-nested', action='store_true',
                        help='Regenerate manuscript outputs without the separate 100-repeat nested validation.')
    args = parser.parse_args()
    root = Path(__file__).resolve().parent
    os.environ['SKIP_NESTED_CV'] = '1' if args.skip_nested else '0'
    os.environ['MPLBACKEND'] = 'Agg'
    os.environ['OPENBLAS_NUM_THREADS'] = '1'
    os.environ['OMP_NUM_THREADS'] = '1'
    os.chdir(root)
    for path in sorted(root.glob('0[1-4]_*.ipynb')):
        print(f'Running {path.name}', flush=True)
        notebook = json.loads(path.read_text(encoding='utf-8'))
        namespace = {'__name__': '__main__'}
        for cell in notebook['cells']:
            if cell['cell_type'] == 'code':
                exec(compile(''.join(cell['source']), path.name, 'exec'), namespace)
        print(f'Completed {path.name}', flush=True)
    print('Results saved in results/.', flush=True)


if __name__ == '__main__':
    main()
