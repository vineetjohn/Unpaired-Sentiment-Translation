from os import walk
from os.path import join
import json

test_folder = "temp_negative"
output_folder = "output"

file_paths = []
for (dirpath, dirnames, filenames) in walk(test_folder):
    file_paths.extend([join(dirpath, x) for x in filenames])


source_pos_path = join(output_folder, "source_pos.txt")
source_neg_path = join(output_folder, "source_neg.txt")
target_pos_path = join(output_folder, "target_pos.txt")
target_neg_path = join(output_folder, "target_neg.txt")

count = 0
with open(source_pos_path, 'w') as source_pos_file, \
        open(source_neg_path, 'w') as source_neg_file, \
        open(target_pos_path, 'w') as target_pos_file, \
        open(target_neg_path, 'w') as target_neg_file:
    for file_path in file_paths:
        with open(file_path) as test_file:
            for json_string in test_file:
                test_json = json.loads(json_string.strip())
                src_sent = test_json['example']
                tgt_sent = test_json['generated']
                tgt_score = test_json['target_score']

                if tgt_score:
                    source_neg_file.write("{}\n".format(src_sent))
                    target_pos_file.write("{}\n".format(tgt_sent))
                else:
                    source_pos_file.write("{}\n".format(src_sent))
                    target_neg_file.write("{}\n".format(tgt_sent))

                count += 1

                if not count % 1000:
                    print("Sentences processed: {}".format(count))

print("Processing complete")
