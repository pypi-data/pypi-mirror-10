========
Usage
========

To use Hexes in a project::

    from hexes import (
        Application,
        Box,
        Style,
    )

    root = Box(
        title="Root",
        children=(
            Box(
                title="A",
                style=Style(
                    min_height=10,
                    height=10,
                    layout=Style.Layout.Horizontal,
                ),
                children=(
                    Box(
                        title="AA",
                        style=Style(
                            min_height=2,
                        ),
                        children=(
                            Box(title="AAA"),
                            Box(title="AAB"),
                        ),
                    ),
                    Box(
                        title="AB",
                        style=Style(
                            min_height=2,
                        ),
                    ),
                ),
            ),
            Box(
                title="B",
                style=Style(
                    min_height=2,
                    height=5,
                ),
            ),
            Box(
                title="C",
                style=Style(min_height=2),
                children=(
                    Box(
                        title="CA",
                        style=Style(min_height=2),
                    ),
                    Box(
                        title="CB",
                        style=Style(min_height=2),
                        children=(
                            Box(
                                title="CBA",
                                style=Style(min_height=2),
                            ),
                        ),
                    ),
                ),
            ),
        ),
    )

    with Application(root=root) as app:
        app.register('q', app.quit)
        app.run()

    print('\n'.join(app.logs))


Right now, all it does is draw boxes, lay them out, and resize them. Don't
worry, this is very alpha and will grow into a beautiful flower.

-------------
Musings on the future
-------------

What sorts of widgets are important in a terminal app?

* Text areas
* Scrollable text areas
* Auto-scrolling text areas (as for chat or Twitter feed)
* Text input areas
* Box-model boxes within boxes

These widgets should be relatively smart, knowing their own dimensions, when to
resize, how to listen to things (some sort of data-binding model here?), how to
style themselves, etc.

The first step is to get a working box-model.

Make a tree-like strucutre that can then be rendered.

Then add attributes like width that can allow a more complex box layout.
Basically doing responsive design.

Then bundle width up with some other things (border, max height, text style)
into a Style object that gets passed in.

Boxes should behave like HTML boxes to an extent, shrink-wrapping to contents'
height.

Then add databinding: the content of this box is this value, two way if the box
is writable. This will require making a particular object, probably with some
descriptor shenanigans.

This is kinda MVC, but I'm flattening the M and C a bit, as I don't care about
their distinction as much. Eventually I may.
