def get_aq_rating(aq_value):
    match aq_value:
        case 1:
            return 'Good'
        case 2:
            return 'Fair'
        case 3:
            return 'Moderate'
        case 4:
            return 'Poor'
        case 5:
            return 'Very Poor'
