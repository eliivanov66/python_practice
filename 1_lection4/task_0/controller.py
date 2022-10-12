import model_sum, model_mult, model_sub, model_div
import view

def button_click():
    value_a = view.get_value()
    value_b = view.get_value()
    model_sum.init(value_a, value_b)
    result = model_sum.action()
    view.view_data(result, "Сумма")
    
    model_sub.init(value_a, value_b)
    result = model_sub.action()
    view.view_data(result, "Разность")

    model_mult.init(value_a, value_b)
    result = model_mult.action()
    view.view_data(result, "Произведение")

    model_div.init(value_a, value_b)
    result = model_div.action()
    view.view_data(result, "Частное")