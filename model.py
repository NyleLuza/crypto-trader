import tensorflow as tf
from data_prep import final_df as data
import numpy as np
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from keras import Sequential
from keras import LSTM, Dense, Dropout
