This demonstrates where append of two BufferDataSets (the implementation of QDataSet
where the data is in a Java NIO buffer, possibly backed by the file without taking
any RAM memory) is incorrect when trim and then append is used.

See https://sourceforge.net/p/autoplot/bugs/2414/
