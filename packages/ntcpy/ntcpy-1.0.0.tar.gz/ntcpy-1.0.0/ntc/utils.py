def rgb(color: str, divider=1):
    return (
        int(color[1:3], 16) / divider,
        int(color[3:5], 16) / divider,
        int(color[5:7], 16) / divider,
    )


def hsl(color: str):
    r, g, b = rgb(color, 255)

    min_ = min((r, g, b))
    max_ = max((r, g, b))
    delta = max_ - min_

    h = 0.0
    s = 0
    l = (min_ + max_) / 2  # noqa: E741

    if l > 0 and l < 1:
        s = delta / (2 * l if l < 0.5 else 2 - 2 * l)

    if delta > 0:
        if max_ == r and max_ != g:
            h += (g - b) / delta
        if max_ == g and max_ != b:
            h += 2 + (b - r) / delta
        if max_ == b and max_ != r:
            h += 4 + (r - g) / delta

        h /= 6

    return h * 255, s * 255, l * 255
