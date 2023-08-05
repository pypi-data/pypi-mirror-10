import curses
import re


class Screen(object):
    """
    Class to track basic state of the screen.  This constructs the necessary
    curses resources to allow us to do the ASCII animations.

    Note that all you really need to do with this class is instantiate it
    with the window object returned by the curses wrapper() method and the
    required height for your screen buffer.  This latter is important if you
    plan on using any Effects that will scroll the screen vertically (e.g.
    Scroll).  It must be big enough to handle the full scrolling of your
    selected Effect.
    """

    def __init__(self, win, height=200):
        """
        Constructor.

        :param win: The window object as returned by the curses wrapper method.
        :param height: The height of the screen buffer to be used.
        """
        # Save off the screen details and se up the scrolling pad.
        self._screen = win
        (self.height, self.width) = self._screen.getmaxyx()
        self.buffer_height = height
        self._pad = curses.newpad(self.buffer_height, self.width)

        # Set up basic colour schemes.
        for i in range(curses.COLOR_RED, curses.COLOR_WHITE):
            curses.init_pair(i, i, curses.COLOR_BLACK)

        # Disable the cursor.
        curses.curs_set(0)

        # Non-blocking key checks.
        self._pad.nodelay(1)

        # Ensure that the screen is clear and ready to go.
        self._start_line = None
        self.clear()

    @property
    def start_line(self):
        """
        :return: The start line of the top of the window in the display buffer.
        """
        return self._start_line

    @property
    def dimensions(self):
        """
        :return: The full dimensions of the display buffer as a (height,
            width) tuple.
        """
        return self._pad.getmaxyx()

    def scroll(self):
        """
        Scroll the Screen up one line.
        """
        self._start_line += 1

    def clear(self):
        """
        Clear the Screen of all content.
        """
        self._pad.clear()
        self._start_line = 0

    def refresh(self):
        """
        Refresh the screen.
        """
        (self.height, self.width) = self._screen.getmaxyx()
        self._pad.refresh(self._start_line,
                          0,
                          0,
                          0,
                          self.height - 1,
                          self.width - 1)

    def get_key(self):
        """
        Check for a key without waiting.
        """
        return self._pad.getch()

    def getch(self, x, y):
        """
        Get the character at the specified location.

        :param x: The column (x coord) of the character.
        :param y: The row (y coord) of the character.

        :return: The ASCII code of the character at the location.
        """
        return self._pad.inch(y, x)

    def putch(self, text, x, y, colour=0, attr=0, transparent=False):
        """
        Print the text at the specified location using the
        specified colour and attributes.

        :param text: The (single line) text to be printed.
        :param x: The column (x coord) for the start of the text.
        :param y: The line (y coord) for the start of the text.
        :param colour: The colour of the text to be displayed.
        :param attr: The cell attribute of the text to be displayed.
        :param transparent: Whether to print spaces or not, thus giving a
            transparent effect.

        See curses for definitions of the colour and attribute values.
        """
        if y < 0:
            return
        if x < 0:
            text = text[-x:]
            x = 0
        if x + len(text) >= self.width:
            text = text[:self.width - x]
        if len(text) > 0:
            if transparent:
                for i, c in enumerate(text):
                    if c != " ":
                        self._pad.addch(
                            y, x+i, c, curses.color_pair(colour) | attr)
            else:
                self._pad.addstr(y, x, text, curses.color_pair(colour) | attr)

    def centre(self, text, y, colour=0, attr=0):
        """
        Centre the text on the specified line (y) using the optional
        colour and attributes.

        :param text: The (single line) text to be printed.
        :param y: The line (y coord) for the start of the text.
        :param colour: The colour of the text to be displayed.
        :param attr: The cell attribute of the text to be displayed.

        See curses for definitions of the colour and attribute values.

        This function will also convert ${n} into colour attribute n for any
        subseqent text in the line, thus allowing multi-coloured text.
        """
        segments = [["", colour]]
        line = text
        while True:
            match = re.match(r"(.*?)\$[{](\d+)[}]", line)
            if match is None:
                break
            segments[-1][0] = match.group(1)
            segments.append(["", int(match.group(2))])
            line = line[len(match.group(0)):]
        segments[-1][0] = line
        total_width = sum([len(x[0]) for x in segments])

        x = (self.width - total_width)/2
        for (text, style) in segments:
            self.putch(text, x, y, style, attr)
            x += len(text)

    def is_visible(self, x, y):
        """
        Return whether the specified location is on the visible screen.

        :param x: The column (x coord) for the location to check.
        :param y: The line (y coord) for the location to check.
        """
        return ((x >= 0) and
                (x <= self.width) and
                (y >= self._start_line) and
                (y < self._start_line + self.height))

    def play(self, scenes):
        """
        Play a set of scenes.

        :param scenes: a list of :py:obj:`.Scene` objects to play.
        """
        while True:
            for scene in scenes:
                frame = 0
                if scene.clear:
                    self.clear()
                scene.reset()
                while frame < scene.duration:
                    # self.putch(
                    #    str(scene.duration - frame) + " ", 0, self._start_line)
                    frame += 1
                    for effect in scene.effects:
                        effect.update(frame)
                    self.refresh()
                    c = self.get_key()
                    if c in (ord("X"), ord("x")):
                        return
                    if c in (ord(" "), ord("\n")):
                        break
                    curses.napms(50)
