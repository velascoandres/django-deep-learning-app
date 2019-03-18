def predecir(ruta_imagen):
    from keras.applications.resnet50 import ResNet50
    from keras.preprocessing import image
    from keras.applications.resnet50 import preprocess_input, decode_predictions
    import numpy as np

    model = ResNet50(weights='imagenet')
    img_path = ruta_imagen
    img = image.load_img(img_path, target_size=(224, 224))
    x = image.img_to_array(img)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)

    preds = model.predict(x)
    # decode the results into a list of tuples (class, description, probability)
    # (one such list for each sample in the batch)
    resultados = decode_predictions(preds, top=3)[0][0]
    descripcion = resultados[1]
    presicion = resultados[2]
    return {
        'descripcion': descripcion,
        'presicion': presicion*100
    }
