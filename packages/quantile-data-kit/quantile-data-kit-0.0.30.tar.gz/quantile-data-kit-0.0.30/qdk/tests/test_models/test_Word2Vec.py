from gensim.models import Word2Vec
from qdk.models import Word2VecModel


def test_word2vec_model():
    X = [["a", "b"]]

    # Instanciate the model
    w2v_model = Word2VecModel(
        vector_size=5,
        min_count=1,
    )

    # Make sure there is no fitted model yet
    assert w2v_model.model == None

    # Fit the model
    w2v_model.fit(X)

    # Make sure the model is fitted now
    assert isinstance(w2v_model.model, Word2Vec)

    # Test the fit_transform functionality
    assert type(w2v_model.fit_transform(X)) == list
