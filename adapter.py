import json

train_review_file_path = "data/yelp/reviews-train.txt"
train_label_file_path = "data/yelp/sentiment-train.txt"
test_review_file_path = "data/yelp/reviews-test.txt"
test_label_file_path = "data/yelp/sentiment-test.txt"

output_train_file_path = "train/yelp.txt"
output_test_file_path = "test/yelp.txt"


def write_new_file(review_file_path, label_file_path, output_file_path):
    with open(review_file_path) as review_file, \
            open(label_file_path) as label_file, \
            open(output_file_path, 'w') as output_file:
        for review, sentiment in zip(review_file, label_file):
            record = dict()
            record["review"] = review.strip()
            record["score"] = 5 if sentiment.strip() == "pos" else 1
            output_file.write("{}\n".format(json.dumps(record)))

write_new_file(train_review_file_path, train_label_file_path, output_train_file_path)
write_new_file(test_review_file_path, test_label_file_path, output_test_file_path)
