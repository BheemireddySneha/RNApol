import sys

parser.add_argument('.sq', type=argparse.FileType('r'), nargs='+')

args = parser.parse_args()
for f in args.file:
    for line in f:
        print(f)
