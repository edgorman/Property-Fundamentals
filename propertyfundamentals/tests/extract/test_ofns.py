from propertyfundamentals.extract.ofns import OFNS


def test_extract():
    ofns = OFNS()
    ofns.get_mean_house_price()
    ofns.get_median_house_price()
