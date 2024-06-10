from main1 import response

from tensorflow.keras.models import load_model
model = load_model('model.h5')

# chat with bot
print("Note: Enter 'quit' to break the loop.")
while True:
    input_ = input('You: ')
    if input_.lower() == 'quit':
        break
    res, typ = response(input_,model)
    print('Bot: {} -- TYPE: {}'.format(res, typ))
    print()