f = [[255, 255, 255]
    ,[255, 0, 255]
    ,[255, 255, 255]]

g = [[250, 250, 250]
     ,[250, 1, 250]
     ,[250, 250, 250]]


def me(f, g):
    """ Maximum Error (ME) """
    max_error = 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            error = abs(f[i][j] - g[i][j])
            if error > max_error:
                max_error = error
    return max_error

def mae(f, g):
    """ Mean Absolute Error (MAE) """
    total_error = 0
    count = 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            error = abs(f[i][j] - g[i][j])
            total_error += error
            count += 1
    return total_error / count

def mse(f, g):
    """ Mean Squared Error (MSE) """
    total_error = 0
    count = 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            error = (f[i][j] - g[i][j]) ** 2
            total_error += error
            count += 1
    return total_error / count

def rmse(f, g):
    """ Root Mean Squared Error (RMSE) """
    return mse(f, g) ** 0.5

def jaccard_coefficient(f, g, tolerance=0):
    """ Jaccard Coefficient """
    t = tolerance
    sum = 0
    for i in range(len(f)):
        for j in range(len(f[i])):
            if f[i][j] >= g[i][j] - t and f[i][j] <= g[i][j] + t:
                sum += 1
    
    return sum / (len(f) * len(f[0]))

if __name__ == "__main__":
    print("put the tolerance: ")
    t = input_tolerance = int(input())
    print("ME:", me(f, g))
    print("MAE:", mae(f, g))
    print("MSE:", mse(f, g))
    print("RMSE:", rmse(f, g))
    print("Jaccard Coefficient:", jaccard_coefficient(f, g, t))