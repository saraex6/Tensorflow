# Import `tensorflow` 
import tensorflow as tf

# Initialize two constants
var1 = tf.constant([2,7,5,4])
var2 = tf.constant([5,12,9,1])

# Multiplying all constants together in var1 & var2
result1 = tf.multiply(var1, var2)

# Multiply all constants in var1 by 100
result2 = tf.multiply(var1, 100)

# Multiply all constants in var2 by 10
result3 = tf.multiply(var2, 10)

# Intialize the Session
s1 = tf.Session()

# Print all results
print(s1.run(result1))
print(s1.run(result2))
print(s1.run(result3))
# Close the session
s1.close()