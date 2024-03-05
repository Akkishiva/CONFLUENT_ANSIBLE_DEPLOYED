def read_hash_from_file(file_path):
    try:
        with open(file_path, 'r') as file:
            return file.read().strip()
    except FileNotFoundError:
        print(f"File not found: {file_path}")
        return None

def compare_hashes(file1, file2):
    hash1 = read_hash_from_file(file1)
    hash2 = read_hash_from_file(file2)

    if hash1 is not None and hash2 is not None:
        if hash1 == hash2:
            print("Hash values match.")
        else:
            print("Hash values do not match.")
    else:
        print("Unable to compare hashes.")

# Replace these paths with the actual paths to your files
pretopics_file_path = 'Pretopics_hash.txt'
posttopics_file_path = 'Posttopics_hash.txt'

compare_hashes(pretopics_file_path, posttopics_file_path)
