# concept-map-generator

1. Clone the repo to local machine.

2. Download GLoVe vectors from Stanford's website - 
```
wget https://nlp.stanford.edu/data/wordvecs/glove.6B.zip
```

3. Unzip the file and keep it in the main directory of our codebase with folder name - "glove.6B". It will contain 4 text files - glove.6B.50d.txt, glove.6B.100d.txt, glove.6B.200d.txt, glove.6B.300d.txt

4. Set up Solr - https://www.howtoforge.com/tutorial/how-to-install-and-configure-solr-on-ubuntu-1604/ 

5. Create a Solr Core 
```
sudo su - solr -c "/opt/solr/bin/solr create -c glove"
```

6. Setup the core
```
cd setup
./setup-solr.py
cd ..
```

7. Install the dependencies - 
```
pip install -r requirements.txt
```

8. Index the vectors in the core - the indexer script is also in the setup folder
```
./solr-indexer.py
cd ..
```

TIP: If you wish to delete the documents from a core, you may do the same by running the following link on your web browser - 
```
localhost:8983/solr/glove/update?commit=true&stream.body=%3Cdelete%3E%3Cquery%3E*:*%3C/query%3E%3C/delete%3E
```

9. Run the main script - 
```
python graphbuilder.py
``` 