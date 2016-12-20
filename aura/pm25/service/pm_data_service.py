

from pm25.exceptions.illegal_parameters_exception import PmDataShowIllegalParameterException


def check_params(parameters):
    city = parameters.get('city', None)
    start_date = parameters.get('startDate', None)
    end_date = parameters.get('endDate', None)

    if not (city and start_date and end_date):
        raise PmDataShowIllegalParameterException(message='%s, %s, %s is mandatory.' % (city, start_date, end_date))

    return city, start_date, end_date
