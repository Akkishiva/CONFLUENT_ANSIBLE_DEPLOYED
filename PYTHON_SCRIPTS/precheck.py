from kafka import KafkaAdminClient, errors
import hashlib
import variables

# List of Kafka brokers (bootstrap servers)
admin_client = KafkaAdminClient(bootstrap_servers=variables.bootstrap_servers)
topic_list = admin_client.list_topics()

# Count the number of topics
num_topics = len(topic_list)

# Calculate the hash of the topics using SHA-256
hash_object = hashlib.sha256(str(topic_list).encode())
topics_hash = hash_object.hexdigest()

print(f"Number of topics in the Kafka cluster: {num_topics}")
print(f"Hash of the topics: {topics_hash}")

# Save the hash to a file
with open('Pretopics_hash.txt', 'w') as file:
    file.write(topics_hash)

print("Hash saved to 'Pretopics_hash.txt'")
