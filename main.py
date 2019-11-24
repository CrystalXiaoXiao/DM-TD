import fasttext

# BoW 1
model = fasttext.train_supervised(input="train.txt",
                                  autotuneValidationFile="dev.txt",
                                  autotuneDuration=3600)
model.save_model("model.bin")
print(model.test("test.txt"))

# BoW 2
model = fasttext.train_supervised(input="train.txt",
                                  autotuneValidationFile="test.txt",
                                  autotuneDuration=3600)
model.save_model("model2.bin")
print(model.test("dev.txt"))

# FastText 1
model = fasttext.train_supervised(input="train.txt",
                                  autotuneValidationFile="dev.txt",
                                  autotuneDuration=3600,
                                  dim=300,
                                  pretrainedVectors='cc.vi.300.vec')
model.save_model("model3.bin")
print(model.test("test.txt"))

# FastText 2
model = fasttext.train_supervised(input="train.txt",
                                  autotuneValidationFile="test.txt",
                                  autotuneDuration=3600,
                                  dim=300,
                                  pretrainedVectors='cc.vi.300.vec')
model.save_model("model4.bin")
print(model.test("dev.txt"))

# word2vec 300
model = fasttext.train_supervised(input="train.txt",
                                  autotuneValidationFile="dev.txt",
                                  autotuneDuration=3600,
                                  dim=300,
                                  pretrainedVectors='baomoi.vn.model.bin')
model.save_model("model5.bin")
print(model.test("test.txt"))

# word2vec 400
model = fasttext.train_supervised(input="train.txt",
                                  autotuneValidationFile="dev.txt",
                                  autotuneDuration=3600,
                                  dim=300,
                                  pretrainedVectors='baomoi.model.bin')
model.save_model("model6.bin")
print(model.test("test.txt"))