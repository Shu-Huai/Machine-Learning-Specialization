import matplotlib.pyplot as plt
import numpy as np
import tensorflow as tf

plt.style.use('deeplearning.mplstyle')


def load_data():
    X = np.load("./data/X.npy")
    y = np.load("./data/y.npy")
    return X, y


def plt_act_trio():
    X = np.linspace(-5, 5, 100)
    fig, ax = plt.subplots(1, 3, figsize=(6, 2))
    widgvis(fig)
    ax[0].plot(X, tf.keras.activations.linear(X))
    ax[0].axvline(0, lw=0.3, c="black")
    ax[0].axhline(0, lw=0.3, c="black")
    ax[0].set_title("Linear")
    ax[1].plot(X, tf.keras.activations.sigmoid(X))
    ax[1].axvline(0, lw=0.3, c="black")
    ax[1].axhline(0, lw=0.3, c="black")
    ax[1].set_title("Sigmoid")
    ax[2].plot(X, tf.keras.activations.relu(X))
    ax[2].axhline(0, lw=0.3, c="black")
    ax[2].axvline(0, lw=0.3, c="black")
    ax[2].set_title("ReLu")
    fig.suptitle("Common Activation Functions", fontsize=14)
    fig.tight_layout(pad=0.2)
    plt.show()


def widgvis(fig):
    fig.canvas.toolbar_visible = False
    fig.canvas.header_visible = False
    fig.canvas.footer_visible = False


def display_errors(model, X, y):
    f = model.predict(X)
    yhat = np.argmax(f, axis=1)
    _ = yhat != y[:, 0]
    idxs = np.where(yhat != y[:, 0])[0]
    if len(idxs) == 0:
        print("no errors found")
    else:
        cnt = min(8, len(idxs))
        fig, ax = plt.subplots(1, cnt, figsize=(5, 1.2))
        fig.tight_layout(pad=0.13, rect=[0, 0.03, 1, 0.80])
        widgvis(fig)
        for i in range(cnt):
            j = idxs[i]
            X_reshaped = X[j].reshape((20, 20)).T
            ax[i].imshow(X_reshaped, cmap='gray')
            prediction = model.predict(X[j].reshape(1, 400))
            prediction_p = tf.nn.softmax(prediction)
            yhat = np.argmax(prediction_p)
            ax[i].set_title(f"{y[j, 0]},{yhat}", fontsize=10)
            ax[i].set_axis_off()
            fig.suptitle("Label, yhat", fontsize=12)
    return len(idxs)


def display_digit(X):
    fig, ax = plt.subplots(1, 1, figsize=(0.5, 0.5))
    widgvis(fig)
    X_reshaped = X.reshape((20, 20)).T
    ax.imshow(X_reshaped, cmap='gray')
    plt.show()


def plot_loss_tf(history):
    fig, ax = plt.subplots(1, 1, figsize=(4, 3))
    widgvis(fig)
    ax.plot(history.history['loss'], label='loss')
    ax.set_ylim([0, 2])
    ax.set_xlabel('Epoch')
    ax.set_ylabel('loss (cost)')
    ax.legend()
    ax.grid(True)
    plt.show()
