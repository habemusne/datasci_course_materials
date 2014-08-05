import MapReduce
import sys

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # key: document identifier
    # value: document contents
    book = record[0]
    words = record[1].split()
    for w in words:
      mr.emit_intermediate (w, book)
      # mr.emit_intermediate(w, 1)

def reducer(word, list_of_books):
    # key: word
    # value: list of books
    book_list = list(set(list_of_books))
    mr.emit((word, book_list))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
