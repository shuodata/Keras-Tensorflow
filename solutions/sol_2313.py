plt.plot(range(len(loss_history)), loss_history, 'o', label='Linear Regression Training phase')
plt.ylabel('cost')
plt.xlabel('epoch')
plt.legend()
plt.show()