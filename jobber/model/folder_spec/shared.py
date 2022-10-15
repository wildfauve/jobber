from jobber.template import test

test_location = ["shared"]

templates = [test.shared.config_for_testing, test.shared.db_setup, test.shared.di, test.shared.spark_test_session]
