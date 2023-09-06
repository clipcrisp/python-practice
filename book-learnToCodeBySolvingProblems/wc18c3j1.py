paint = int(input())
bottlecap_paint = int(input())
cap_cost = int(input())

painted_caps = paint // bottlecap_paint
remainder_paint = paint % bottlecap_paint

print((painted_caps * cap_cost) + remainder_paint)
