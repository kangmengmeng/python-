
probs = model.predict(img_data, verbose=False)[0, :, :, :]  # Warm-up
probs = model.predict(img_data, verbose=False)[0, :, :, :]  # Warm-up
start_time = time.time()  # You'd have to do 'import time' at the start of the module
probs = model.predict(img_data, verbose=False)[0, :, :, :]
end_time = time.time()
print("Time spent on the forward pass: {:.3f} s".format(end_time - start_time))
