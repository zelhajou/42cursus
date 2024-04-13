# Style sheet language

## Cascading Style Sheets (CSS)

### Initial reset
```css
html {
    box-sizing: border-box;
    font-size: 16px;
}

*, *:before, *:after {
    box-sizing: inherit;
    margin: 0;
    padding: 0;
    /*outline: 1px dashed blue; /* Debugging purposes */
}
```

```css

```

### CSS Syntax
```css
tag [attributes] #id .class:pseudoclass::pseudoelement {
  property: value;
}
```

### [attributes]
```css
[attr]        /*   : elements with attr attribute present  */
[attr="val"]  : /* elements with attr= attribute with value val  "val" */
[attr~="val"] : /* elements with attr~= that contains val        "abc val xyz" */
[attr|="es"]  : /* elements with attr|= that contains es-*       "en-US es-ES" */
[attr*="val"] : /* elements with attr*= that includes val        "equivalent-is-" */
[attr$="val"] : /* elements with attr$= that ends with val       "in-interval" */
[attr^="val"] : /* elements with attr^= that begins with val     "value-is-..." */
```

### Pseudoclass & Pseudoelements
```css
/* :pseudoclass */
/* LINK */
:link                     : /* links that have not yet been visited */
:visited                  : /* links that has been visited */ 
/* USER ACTION */
:hover                    : /* user move mouse/pointer over element */
:active                   : /* element is being activated by user */
:focus                    : /* element has the focus (foreground) */
/* USER INTERFACE */
:enabled :disabled        : /* on/off input state */
:checked                  : /* elements toggled "on" by user */
:indeterminate            : /* input on indeterminate state */
:read-only                : /* read-write readonly input or modifiable */
:placeholder-shown        : /* inputs that shows placeholder at now */
:default                  : /* default elements for form (input, option, ...) */
:valid/:invalid           : /* userdata pass/not pass check validation */
:in-range :out-of-range   : /* userdata in range/out of range */
:required :optional       : /* elements required/optional for submit */

/* STRUCTURAL */
/* CHILD ELEMENTS */
:first-child      : /* first child of group of elements ~:nth-child(1) */
:last-child       : /* last child of group of elements ~:nth-last-child(1) */

:nth-child(n)         : /* nth child of group of elements  */
:nth-last-child(n)    : /* last nth child of group of elements */ 
:only-child           : /* unique child ~:first-child:last-child */

/* CHILD OF SAME TYPE : */
:first-of-type        : /* first child of same type */
:last-of-type         : /* last child of same type */
:nth-of-type(n)       : /* nth child of same type */
:nth-last-of-type(n)  : /* last nth child (same type) */
:only-of-type         : /* unique child (same type) */
/* OTHERS */
:root                 : /* root element of the document */
:empty                : /* element without contents */

/* OTHERS */ 
:not(x)               : /* not match by x selector */
:target               : /* is the target of anchor URL */
:lang(x)              : /* elements in x language */

/* PSEUDOELEMENTS */
::first-line          : /* first line of text element */
::first-letter        : /* first letter of text element */
```

### RESETTING ALL PROPERTIES
```css
all : initial inherit unset

/* COMMON VALUES */
initial                   : /* property's initial value */
inherit                   : /* computed value on parent */
unset                     : /* initial or inherit (depending) */

/* FONT-RELATIVE SIZES */
em                        : /* computed value on current */
ex                        : /* x-height of lowercase "x" */
ch                        : /* advance measure of "0" glyph */
rem                       : /* computed value on root elem */

/* VIEWPORT SIZES */
vw                        : /* viewport width */
vh                        : /* viewport height % */
vmin                      : /* smaller (vw or vh) */
vmax                      : /* larger (vw or vh) */

/* ABSOLUTE SIZES */
px                        : /* pixels */
cm                        : /* centimeters */
mm                        : /* millimeters */
Q                         : /* quarter-mm */
in                        : /* inches */
pc                        : /* picas */
pt                        : /* points */

/* ANGLES */
deg                       : degrees [0..360]
grad                      : gradians [0..400]
rad                       : radians [0..6.28]
rad                       : turns [0.0..1.0
```

### Font

```css
/** Body Selector which applies properties to whole body <body></body> */
body {
  /* Font-Family */
  font-family: "Segoe UI", Tahoma, sans-serif; /* You can declare multiple fonts. */
  /*if first font doesn't exists other ones will be declared serial wise */

  /* Font-Style */
  font-style: italic;

  /* Font-Variant */
  font-variant: small-caps;

  /* Font-Weight */
  font-weight: bold;

  /* Font-Size */
  font-size: larger;

  /* Font */
  font: style variant weight size family;
}
```

### Text

```css
/* Applies to all tags with class 'container' ex: <div class="container"></div> */
.container {
  /* Text-Align */
  text-align: justify;

  /* Letter-Spacing */
  letter-spacing: 0.15em;

  /* Text-Decoration */
  text-decoration: underline;

  /* Word-Spacing */
  word-spacing: 0.25em;

  /* Text-Transform */
  text-transform: uppercase;

  /* Text-Indent */
  text-indent: 0.5cm;

  /* Line-Height */
  line-height: normal;
}
```

### Background

```css
/* Applies to all tags with id 'wrapper' ex: <div id="wrapper"></div> */
#wrapper {
  /* Background-Image */
  background-image: url("Path");

  /* Background-Position */
  background-position: right top;

  /* Background-Size */
  background-size: cover;

  /* Background-Repeat */
  background-repeat: no-repeat;

  /* Background-Attachment */
  background-attachment: scroll;

  /* Background-Color */
  background-color: fuchsia;

  /* Background */
  background: color image repeat attachment position;
}
```

### Border

```css
/* You can also select multiple items */
div,
.container {
  /* Border-Width */
  border-width: 5px;

  /* Border-Style */
  border-style: solid;

  /* Border-Color */
  border-color: aqua;

  /* Border-Radius */
  border-radius: 15px;

  /* Border */
  border: width style color;
}
```

### Box Model

The CSS box model is a container that wraps around every HTML element. It consists of margins, borders, padding, and the actual content. It is used to create the design and layout of web pages.

```css
.wrapper {
  /* Float */
  float: none;
  /* Clear */
  clear: both;
  /* Display */
  display: block;
  /* Height */
  height: fit-content;
  /* Width */
  width: auto;
  /* Margin */
  margin: top right bottom left;
  /* Padding */
  padding: top right bottom left;
  /* Overflow */
  overflow: hidden;
  /* Visibility */
  visibility: visible;
  /* z-index */
  z-index: 1;
  /* position */
  position: static | relative | fixed | absolute | sticky;

}
```

### Colors

With the help of the color property, one can give color to text, shape, or any other object.

```css
p,
span,
.text {
  /* Color - 1 */
  color: cornsilk;
  /* Color - 2 */
  color: #fff8dc;
  /* Color - 3 */
  color: rgba(255, 248, 220, 1);
  /* Color - 4 */
  color: hsl(48, 100%, 93%);
  /* Opacity */
  opacity: 1;
}
```

### Images

```css
.image {
  width: 300px;           /* Resizes the image to a width of 300px. Height will also resize to keep the image's dimensions. */
  height: 300px;          /* If both width and height are set, the image may stretch. */
  object-fit: cover;      /* Enlarges the image to cover the entire width * height area without stretching or distorting.*/
  object-fit: contain;    /* Shrinks the image so that it's contained in the width * height area. */

  /*  Determines where the image is positioned in the width * height area. */
  object-position: left;
  object-position: right;
  object-position: top;
  object-position: bottom;
}
```

### Template Layout
Specifies the visual look of the content inside a template

```css
/* '*' selects all elements on a page */
* {
  /* Box-Align */
  box-align: start;

  /* Box-Direction */
  box-direction: normal;

  /* Box-Flex */
  box-flex: normal;

  /* Box-Flex-Group */
  box-flex-group: 2;

  /* Box-Orient */
  box-orient: inline;

  /* Box-Pack */
  box-pack: justify;

  /* Box-Sizing */
  box-sizing: margin-box;

  /* max-width */
  max-width: 800px;

  /* min-width */
  min-width: 500px;

  /* max-height */
  max-height: 100px;

  /* min-height */
  min-height: 80px;
}
```

### Table
Table properties are used to give style to the tables in the document. You can change many things like border spacing, table layout, caption, etc.

```css
table {
  /* Border-Collapse */
  border-collapse: separate;

  /* Empty-Cells */
  empty-cells: show;

  /* Border-Spacing */
  border-spacing: 2px;

  /* Table-Layout */
  table-layout: auto;

  /* Caption-Side */
  caption-side: bottom;
}
```

### Columns
These properties are used explicitly with columns of the tables, and they are used to give the table an incredible look.

```css
/* Applies to <table class="nice-table"></table> */
/* Not <table></table> */
table.nice-table {
  /* Column-Count */
  column-count: 10;

  /* Column-Gap */
  column-gap: 5px;

  /* Column-rule-width */
  column-rule-width: medium;

  /* Column-rule-style */
  column-rule-style: dotted;

  /* Column-rule-color */
  column-rule-color: black;

  /* Column-width */
  column-width: 10px;

  /* Column-span */
  column-span: all;
}
```

### List & Markers
List and marker properties are used to customize lists in the document.

```css
li,
ul,
ol {
  /* List-style-type */
  list-style-type: square;

  /* List-style-position */
  list-style-position: 20px;

  /* List-style-image */
  list-style-image: url("image.gif");

  /* Marker-offset */
  marker-offset: auto;
}
```

### Animations
CSS animations allow one to animate transitions or other media files on the web page.

```css
svg,
.loader {
  /* Animation-name */
  animation-name: myanimation;

  /* Animation-duration */
  animation-duration: 10s;

  /* Animation-timing-function */
  animation-timing-function: ease;

  /* Animation-delay */
  animation-delay: 5ms;

  /* Animation-iteration-count */
  animation-iteration-count: 3;

  /* Animation-direction */
  animation-direction: normal;

  /* Animation-play-state */
  animation-play-state: running;

  /* Animation-fill-mode */
  animation-fill-mode: both;
}
```

### Transitions
Transitions let you define the transition between two states of an element.

```css
a,
button {
  /* Transition-property */
  transition-property: none;

  /* Transition-duration */
  transition-duration: 2s;

  /* Transition-timing-function */
  transition-timing-function: ease-in-out;

  /* Transition-delay */
  transition-delay: 20ms;
}
```

### CSS Flexbox

Flexbox is a layout of CSS that lets you format HTML easily. Flexbox makes it simple to align items vertically and horizontally using rows and columns. Items will "flex" to different sizes to fill the space. And overall, it makes the responsive design more manageable.

#### Parent Properties (flex container)

```css
section,
div#wrapper {
  /* display */
  display: flex;

  /* flex-direction */
  flex-direction: row | row-reverse | column | column-reverse;

  /* flex-wrap */
  flex-wrap: nowrap | wrap | wrap-reverse;

  /* flex-flow */
  flex-flow: column wrap;

  /* justify-content */
  justify-content: flex-start | flex-end | center | space-between | space-around;

  /* align-items */
  align-items: stretch | flex-start | flex-end | center | baseline;

  /* align-content */
  align-content: flex-start | flex-end | center | space-between | space-around;
}
```

#### Child Properties (flex items)

```css
p,
span,
h1,
h2,
h3,
h4,
h5,
h6,
a {
    /* order */
    order: 5; /* default is 0 */

    /* flex-grow */
    flex-grow: 4; /* default 0 */

    /* flex-shrink */
    flex-shrink: 3; /* default 1 */

    /* flex-basis */
    flex-basis: | auto; /* default auto */

    /* flex shorthand */
    flex: none | [ <'flex-grow'> <'flex-shrink'>? || <'flex-basis'> ]

    /* align-self */
    align-self: auto | flex-start | flex-end | center | baseline | stretch;
}
```
- [See flexbox in action 1](https://codepen.io/enxaneta/full/adLPwv)
- [See flexbox in action 2](https://the-echoplex.net/flexyboxes/)
- [Detailed Flexbox Tutorial for Beginners](https://www.zachgollwitzer.com/posts/2021/fullstack-developer-series/10-flexbox-crash-course/)
- Tutorial: https://www.samanthaming.com/flexbox30/

### CSS Grid
Grid layout is a 2-Dimensional grid system to CSS that creates complex responsive web design layouts more easily and consistently across browsers.

#### Parent Properties (Grid container)

```css
section,
div#wrapper {
    /* display */
    display: grid | inline-grid;

    /* grid-template-columns */
    grid-template-columns: 12px 12px 12px;

    /* grid-template-rows */
    grid-template-rows: 8px auto 12px;

    /* grid-template */
    grid-template: none | <grid-template-rows> / <grid-template-columns>;

    /* column-gap */
    column-gap: <line-size>;

    /* row-gap */
    row-gap: <line-size>;

    /* grid-column-gap */
    grid-column-gap: <line-size>;

    /* grid-row-gap */
    grid-row-gap: <line-size>;

    /* gap shorthand */
    gap: <grid-row-gap> <grid-column-gap>;

    /* grid-gap shorthand */
    grid-gap: <grid-row-gap> <grid-column-gap>;

    /* justify-items */
    justify-items: start | end | center | stretch;

    /* align-items */
    align-items: start | end | center | stretch;

    /* place-items */
    place-items: center;

    /* justify-content */
    justify-content: start | end | center | stretch | space-around | space-between;

    /* align-content */
    align-content: start | end | center | stretch | space-around | space-between;

    /* place-content */
    place-content: <align-content> / <justify-content>;

    /* grid-auto-columns */
    grid-auto-columns: <track-size> ...;

    /* grid-auto-rows */
    grid-auto-rows: <track-size> ...;

    /* grid-auto-flow */
    grid-auto-flow: row | column | row dense | column dense;

}
```

#### Child Properties (Grid items)

```css
p,
span,
h1,
h2,
h3,
h4,
h5,
h6,
a {
    /* grid-column-start */
    grid-column-start: <number> | <name> | span <number> | span <name> | auto;

    /* grid-column-end */
    grid-column-end: <number> | <name> | span <number> | span <name> | auto;

    /* grid-row-start */
    grid-row-start: <number> | <name> | span <number> | span <name> | auto;

    /* grid-row-end */
    grid-row-end: <number> | <name> | span <number> | span <name> | auto;

    /* grid-column shorthand */
    grid-column: <start-line> / <end-line> | <start-line> / span <value>;

    /* grid-row shorthand */
    grid-row: <start-line> / <end-line> | <start-line> / span <value>;

    /* grid-area */
    grid-area: <name> | <row-start> / <column-start> / <row-end> / <column-end>;

    /* justify-self */
    justify-self: start | end | center | stretch;

    /* align-self */
    align-self: start | end | center | stretch;

    /* place-self */
    place-self: center;
}
```

- THE EXPERIMENTAL LAYOUT LAB: https://labs.jensimmons.com/
- Grid by Example: https://gridbyexample.com/
- Definition and explanation: https://webkit.org/blog/7434/css-grid-layout-a-new-layout-module-for-the-web/
- The Complete CSS Grid Tutorial: https://jst.hashnode.dev/css-grid-tutorial

### MEDIA QUERIES
Using media queries are a popular technique for delivering a tailored style sheet to desktops, laptops, tablets, and mobile phones (such as iPhone and Android phones).

```
|----------------------------------------------------------|
|  Responsive Grid Media Queries - 1280, 1024, 768, 480    |
|   1280-1024   - desktop (default grid)                   |
|   1024-768    - tablet landscape                         |
|   768-480     - tablet                                   |
|   480-less    - phone landscape & smaller                |
|----------------------------------------------------------|
```


```html
<!-- Make Sure you don't forgot to add -->
<meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=no" /> /* within <head> tag  */
```

```css

@media all and (min-width: 1024px) and (max-width: 1280px) { }

@media all and (min-width: 768px) and (max-width: 1024px) { }

@media all and (min-width: 480px) and (max-width: 768px) { }

@media all and (max-width: 480px) { }

/* Small screens - MOBILE */
@media only screen { } /* Define mobile styles - Mobile First */

@media only screen and (max-width: 40em) { } /* max-width 640px, mobile-only styles, use when QAing mobile issues */

/* Medium screens - TABLET */
@media only screen and (min-width: 40.063em) { } /* min-width 641px, medium screens */

@media only screen and (min-width: 40.063em) and (max-width: 64em) { } /* min-width 641px and max-width 1024px, use when QAing tablet-only issues */

/* Large screens - DESKTOP */
@media only screen and (min-width: 64.063em) { } /* min-width 1025px, large screens */

@media only screen and (min-width: 64.063em) and (max-width: 90em) { } /* min-width 1024px and max-width 1440px, use when QAing large screen-only issues */

/* XLarge screens */
@media only screen and (min-width: 90.063em) { } /* min-width 1441px, xlarge screens */

@media only screen and (min-width: 90.063em) and (max-width: 120em) { } /* min-width 1441px and max-width 1920px, use when QAing xlarge screen-only issues */

/* XXLarge screens */
@media only screen and (min-width: 120.063em) { } /* min-width 1921px, xlarge screens */

/*------------------------------------------*/



/* Portrait */
@media screen and (orientation:portrait) { /* Portrait styles here */ }
/* Landscape */
@media screen and (orientation:landscape) { /* Landscape styles here */ }


/* CSS for iPhone, iPad, and Retina Displays */

/* Non-Retina */
@media screen and (-webkit-max-device-pixel-ratio: 1) {
}

/* Retina */
@media only screen and (-webkit-min-device-pixel-ratio: 1.5),
only screen and (-o-min-device-pixel-ratio: 3/2),
only screen and (min--moz-device-pixel-ratio: 1.5),
only screen and (min-device-pixel-ratio: 1.5) {
}

/* iPhone Portrait */
@media screen and (max-device-width: 480px) and (orientation:portrait) {
} 

/* iPhone Landscape */
@media screen and (max-device-width: 480px) and (orientation:landscape) {
}

/* iPad Portrait */
@media screen and (min-device-width: 481px) and (orientation:portrait) {
}

/* iPad Landscape */
@media screen and (min-device-width: 481px) and (orientation:landscape) {
}
```

### CSS Architecture

https://bem-cheat-sheet.9elements.com/

### CSS Tools
- [10015.io](https://10015.io/css-tools)


### CSS Generator

- [Neumorphism/Soft UI CSS shadow generator](https://neumorphism.io/#55b9f3)
- [Pixel Art to CSS](https://www.pixelartcss.com/)
- [CSS Section Separator Generator | wweb.dev](https://wweb.dev/resources/css-separator-generator)
- [Get Waves - Create SVG waves for your next design](https://getwaves.io/)
- [CSS box-shadow examples - CSS Scan](https://getcssscan.com/css-box-shadow-examples)

**Blob:**

- [Fancy Border Radius Generator]([https://9elements.github.io/fancy-border-radius/#30.30.37.30--.)
- [Blobs - Generate beautiful blob shapes for web and flutter apps](https://blobs.app/)
- [Blobmaker](https://www.blobmaker.app/)

**SVG**

- https://svgartista.net/
- https://connoratherton.com/loaders
- https://www.csswand.dev/
- [BGJar | Free svg background image generator for your websites](https://bgjar.com/)
- [Shapefest™ - A massive library of free 3D shapes](https://www.shapefest.com/)
- [Free SVG Maps - amCharts](https://www.amcharts.com/svg-maps/)


**Gradients and colours**

- [CSSGradients](https://cssgradient.io/gradient-backgrounds/)
- [Name that colour](https://chir.ag/projects/name-that-color/)
- [CSS Gradient — Generator, Maker, and Background](https://cssgradient.io/)
- [Gradient Magic](https://www.gradientmagic.com/?fbclid=IwAR1QIAH2jWHUR63BO6fMBa8lAfSoHlo8BkTXFGNVAJERYu6fZcGxI8WjbE0)

[css-doodle](https://css-doodle.com/)
https://fffuel.co/


#### Github repos

- https://github.com/troxler/awesome-css-frameworks
- https://autoprefixer.github.io/
