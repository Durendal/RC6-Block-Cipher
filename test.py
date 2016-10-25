import rc6

testString = "This is a test string that is more than 16 chars and spans over multiple blocks"
testKey = "abcdefghijklmnopqrstuvqxyz"
res, str = rc6.encrypt(testString, testKey)
print "Test String: %s, Key: %s" % (testString, testKey)
res2, str2 = rc6.decrypt(str, testKey)
print "len(testString): %d" % len(testString)
print "len(str): %d" % len(str)
print "len(str2): %d" % len(str2)
print "Before: ", str
print "After: ", str2