from clarifai import rest
api = rest.ApiClient()
api.addInputs([rest.Image(url="https://samples.clarifai.com/metro-north.jpg", ID="some-id")])

