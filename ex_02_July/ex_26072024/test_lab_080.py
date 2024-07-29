# Integration scenarios

# 1.Verify create booking --> patch request -->verify the firstname  is updated
# 2.Verify create booking --> patch request -->verify the last name  is updated
# 3.Verify create booking --> patch request -->verify the depositprice  is updated to False
# 4.Create a booking --> delete booking with id --> verify by get to check it does not exist
# 5.Get an existing booking from id --> update it and verify it is updating.
# 6.Invalid creation --> create booking with a wrong payload
#7.Try to update a deleted id and you should get a 404
#8.Create a booking and delete it
