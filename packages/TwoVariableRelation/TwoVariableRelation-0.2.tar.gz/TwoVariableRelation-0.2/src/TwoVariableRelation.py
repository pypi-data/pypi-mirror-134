def polynomial_model(degree,X,Y):
    import pandas as pd
    import xlrd
    import numpy as np
    from scipy.stats import chi2
    from sklearn.preprocessing import PolynomialFeatures
    from sklearn.linear_model import LinearRegression
    from sklearn.metrics import mean_squared_error, r2_score
    pd.set_option('display.colheader_justify', 'center')
    
    df = pd.DataFrame({'X':X,'Y':Y})
    data=df.copy()
    data= data.to_numpy()
    ##Applying outlier treatment on entire dataframe
    covariance  = np.cov(data, rowvar=False)
     # Covariance matrix power of -1
    covariance_pm1 = np.linalg.matrix_power(covariance, -1)
    # Center point
    centerpoint = np.mean(data, axis=0)
    # Distances between center point and 
    distances = []
    for i, val in enumerate(data):
          p1 = val
          p2 = centerpoint
          distance = (p1-p2).T.dot(covariance_pm1).dot(p1-p2)
          distances.append(distance)
    distances = np.array(distances)
    
    # Cutoff (threshold) value from Chi-Sqaure Distribution for detecting outliers 
    cutoff = chi2.ppf(0.95, data.shape[1])
    
    # Index of outliers
    outlierIndexes = np.where(distances > cutoff )
    df=df.drop(df.index[outlierIndexes])
    df=df.reset_index(drop=True)
    
    
    X=df.iloc[:,0].values
    Y=df.iloc[:,1].values
    
    X=X.reshape(-1,1)
    Y=Y.reshape(-1,1)
    
    train=round(len(X)*0.7)
    
    X_train, X_test = X[0:train], X[train:]
    Y_train, Y_test = Y[0:train], Y[train:]
    accuracy_actual=sum(Y_test)
    
    
    polynomial=[]
    rmse_train=[]
    rmse_test=[]
    accuracy=[]
    r2_train=[]
    r2_test=[]
    
    for i in range(degree+1):
        
        poly_features = PolynomialFeatures(degree=i)
        
        X_poly_train = poly_features.fit_transform(X_train)
        poly_model = LinearRegression()
        poly_model.fit(X_poly_train,Y_train)
        
        y_predicted_train = poly_model.predict(X_poly_train)
        y_predicted_test = poly_model.predict(poly_features.fit_transform(X_test))
        
        
        rmse_train_ = np.sqrt(mean_squared_error(Y_train, y_predicted_train))
        rmse_test_=np.sqrt(mean_squared_error(Y_test, y_predicted_test))
        accuracy_predicted=sum(y_predicted_test)
        accuracy_test=(1-(abs(accuracy_actual-accuracy_predicted)/accuracy_actual))*100
        
        r2_train_=r2_score(Y_train, y_predicted_train)
        r2_test_=r2_score(Y_test, y_predicted_test)
        
        polynomial.append(i)
        rmse_train.append(rmse_train_)
        rmse_test.append(rmse_test_)
        r2_train.append(r2_train_)
        r2_test.append( r2_test_)
        accuracy.append(accuracy_test)
        
        
    order_dataframe = pd.DataFrame({'Order':polynomial,'RMSE train':rmse_train,'RMSE test':rmse_test,
                                    'Rsquare train':r2_train,'Rsquare test':r2_test,
                                    'Test Accuracy':accuracy})
    order_dataframe['Test Accuracy'] =  order_dataframe['Test Accuracy'].str.get(0)
    order_dataframe=order_dataframe.round(3)
    blankIndex=[''] * len(order_dataframe)
    order_dataframe.index=blankIndex
    order_dataframe['Proportion']=order_dataframe['Test Accuracy']/order_dataframe['RMSE train']
    order_dataframe = order_dataframe.sort_values(by=['Proportion'],ascending=False)
    Order=order_dataframe['Order'].iloc[0]
    order_dataframe['Test Accuracy'] = order_dataframe['Test Accuracy'].map("{:,.3f}%".format)
    order_dataframe = order_dataframe[['Order', 'RMSE train','RMSE test','Rsquare train',
                                     'Rsquare test', 'Test Accuracy']]
    order_dataframe = order_dataframe.sort_values(by=['Order'])
    print(order_dataframe)
    print("Model is best fitted at polynomial degree",Order)
    











