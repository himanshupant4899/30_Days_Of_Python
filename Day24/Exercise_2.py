# Below you'll find an itemgetter function that takes in a collection, and either a key or index. Catch any instances
# of KeyError or IndexError, and write the exception to a file called log.txt, along with the arguments that caused
# this issue. Once you have written to the log file, reraise the original exception.

def itemgetter(collection, identifier):
    try:
        return collection[identifier]
    except KeyError:
        with open("log.txt", "a") as logs:
            logs.write(f"Exception: {KeyError} - collection: {collection}, identifier: {identifier}\n")
            raise
    except IndexError:
        with open("log.txt", "a") as logs:
            logs.write(f"Exception: {IndexError} - collection: {collection}, identifier: {identifier}\n")
            raise


lst = ["a", "b", "c", "d"]
ind = 9
itemgetter(lst, ind)
