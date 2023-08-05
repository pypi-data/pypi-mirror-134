import ruckus
import numpy as np
import unittest

n_samples = np.random.choice(10)+1
n_features = np.random.choice(10)+1
n_samples_2 = np.random.choice(10)+1
n_features_2 = np.random.choice(10)+1
n_samples_3 = np.random.choice(10)+1

Xtest = np.random.rand(n_samples*n_features).reshape([n_samples,n_features])
Ytest = np.random.rand(n_samples_2*n_features).reshape([n_samples_2,n_features])
Ztest = np.random.rand(n_samples*n_samples_2*n_features).reshape([n_samples,n_samples_2,n_features])

class TestRKHSMethods(unittest.TestCase):
    def test_fit(self):
        rkhs = ruckus.RKHS()
        rkhs.fit(Xtest)
        np.testing.assert_array_equal(rkhs.X_fit_,Xtest)
        self.assertEqual(rkhs.shape_in_,Xtest.shape[1:])
        self.assertEqual(rkhs.shape_out_,Xtest.shape[1:])

    def test_transform(self):
        rkhs = ruckus.RKHS()
        rkhs.fit(Xtest)
        Y = rkhs.transform(Xtest)
        np.testing.assert_array_equal(Xtest,Y)
        self.assertEqual(rkhs.shape_out_,Y.shape[1:])

    def test_kernel(self):
        rkhs = ruckus.RKHS()
        rkhs.fit(Xtest)
        K = rkhs.kernel(Xtest)
        np.testing.assert_allclose(K,Xtest@Xtest.T,rtol=1e-10,err_msg='Same-argument kernel fails')
        K = rkhs.kernel(Xtest,Ytest)
        np.testing.assert_array_equal(K,Xtest@Ytest.T)

    def test_gen_sample(self):
        rkhs = ruckus.RKHS()
        rkhs.fit(Xtest)
        P = rkhs._gen_sample(Ytest[0],size=n_samples_2)
        self.assertEqual(P.shape,Ytest.shape)
        np.testing.assert_array_equal(P,np.array([Ytest[0]]*n_samples_2))

    def test_sample(self):
        rkhs = ruckus.RKHS()
        rkhs.fit(Xtest)
        P = rkhs.sample(Ztest,size=n_samples_3)
        self.assertEqual(P.shape,(n_samples_3,)+Ztest.shape)
        np.testing.assert_array_equal(P,np.array([Ztest]*n_samples_3))

class TestProductMethods(unittest.TestCase):
    def test_fit(self):
        rkhs1 = ruckus.RKHS()
        rkhs2 = ruckus.RKHS()
        prod_rkhs = ruckus.ProductRKHS([rkhs1,rkhs2])
        prod_rkhs.fit(Xtest)
        np.testing.assert_array_equal(prod_rkhs.X_fit_,Xtest)
        self.assertEqual(prod_rkhs.shape_in_,Xtest.shape[1:])
        self.assertEqual(prod_rkhs.shape_out_,Xtest.shape[1:]*2)

if __name__ == '__main__':
    unittest.main()