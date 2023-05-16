# Porting Notes

As per [Notecarrier-B](../../../Notecarrier-B/KiCad_format/documentation/PortingNotes.md), except:

## Project

The complexity falls neatly between Notecarrier-B (single sheet) and Notecarrier-F (multiple sheets, which I upconverted to be hierarchial). At two sheets, introducing hierarchy is unnecessary. Nonetheless, KiCad still leans towards having a "root" (top-level) sheet that references other sheets in the project. This works out nicely, providing an opportunity to port the mechanical components on the original "revision" sheet, which then acts as a "table of contents", maintaining the name and ordering of the two main schematic sheets. We can then take advantage of the "flat" project style described in the [KiCad docs](https://docs.kicad.org/7.0/en/eeschema/eeschema.html):

> Flat: a sub-case of a simple hierarchy, without connections between subsheets and their parent. Flat hierarchies can be used to represent a non-hierarchical design.


## Schematic

- Some of the symbols convey useful information, so have been ported.
	- Eg. `3xAA`, `B2B-PH-SM4-TBT(LF)(SN)`.
	- The USB micro and B symbols are good too, but for now I will stick with the convention in Notecarrier-B to avoid creating a new one.
		- This has the side-effect of losing the subtle visual indication that one is vertical and one is horizontal, but is in keeping with the convention that schematic symbols don't include this sort of detail.
- KiCad only supports two orientations of schematic text, so I've flipped `L7` and `L8` 180°.

### BOM

- Extracting the necessary information from the existing design files was cumbersome, so a specific BOM was generated:
	- Tools --> Bill Of Materials.
	- Check "Process entire design" and "Use instances".
	- Set "Header" to: `Reference\tValue\tCaratteristiche\tDescription\tMPN\tNote\tPkg Type\tDistributor\tTemp Range\tColor\tDatabase\tDesignator`.
	- Set "Combined property string:" to: `{Reference}\t{Value}\t{Caratteristiche}\t{Description}\t{MPN}\t{Note}\t{Pkg Type}\t{Distributor}\t{Temp Range}\t{Color}\t{Database}\t{Designator}`
	- Unselect "Place each part entry on a separate line.
	- Click "OK".
	- Open output file in a spreadsheet viewer and then compare to and copy-paste between KiCad's "Symbol Field Table".
- Again, some of the original text is Italian and I've not undertaken a translation. However, some of the parts match parts in Notecarrier-B or -F which have already been translated (eg. screw, diode, fuse, micro-usb connector and ICs). So where there's no chance of introducing falsehoods, I've integrated the existing translations.
	- Over time I've picked up on some of the key Italian abbreviations which pop up regularly in names and descriptions, like `MDS` or `M/D`:
		- Maschio (M): male
		- Femmina (F): female
		- Dritto (D): straight (vertical)
		- Orizzontale (O): horizontal
	- So "F/D" is female/straight, "F/90°" is female/right-angle, "MDS" is male/vertical and "MOS" is male/horizontal. I don't know what the final "S" is. Maybe single row?


## PCB

### Footprints

- Again, the design files don't include the libraries so the schematic files don't have access to their own footprints, so the footprints have to be extracted from the PCB file.
	- Best way I've found is Export --> More --> Libraries and just export everything.
	- Then each footprint can be opened via its `.dra` file.
	- And each pad can be viewed via Tools --> Padstack --> Modify Design Padstack.
- The `J-22-0254-FDT-H0508_EDGE` footprint uses a complicated pad stack to both add a castellated hole alongside the through-hole, and make the pad on the back side bigger. Typically in KiCad you would do complicated pad stacks piecewise by putting pads on top of pads, but still I ran into trouble because THT pads don't allow a different front/back pad. Instead of adding a 3rd pad of type SMD, I opted to use two THT pads to capture the two holes, and edit the file by hand to change one to front only and one to back only so the two different pad sizes can be captured.
	- Some discussion [here](https://forum.kicad.info/t/kicad-6-0-footprint-editor-how-to-set-pads-as-one-sided/35167).
- Can't see the difference between `J-5-0065-FOS-USB10118192-NOF` and the existing `J-5-0065-FOS-MICROUSB10118192` so am substituting the latter for now.
- `J-NANOSIM-SF72S006VBA` looks the same as the existing, except for the addition of some complex keepout voids. They don't affect the manufacturing output and are of unknown value, so I've not ported them.
- I used the existing `SOT666` and `J-NANOSIM-SF72S006VBA` footprints but in early validation realised some improvements. They both derived features from existing Altium footprints, which had elements on Mechanical layers 1, 5, 13, 15, 17, 18, 19, 26 and 255. Naturally this was a nightmare to convert to meaningful layers.
	- While it's not possible to be "wrong" given there's no one-to-one mapping for non-manufactured layers, on reflection it would suit both projects better to move some elements to other layers.
		- For `J-NANOSIM-SF72S006VBA` the elements I introduced to the `F.Silkscreen` layer (originally in "Mechanical 255") I will move to the `User.Drawings` since it's a better match to be visible in manufacturing documents, not on the board. While the OrCAD footprint does have these on the silkscreen, that is not how it is used on the board. And the elements originally on "Mechanical 17" (pin numbers) I will move to `User.Comments` to distinguish them from the `User.Drawings` (originally "Mechanical 18"). `F.Fab` will still get the component outline (which was also on "Mechanical 18", unlike other footprints that have it on "Mechanical 13"!).
			- This is a sufficient compromise between the two source footprints, but there's still room for improvement if the footprint conventions were to be consolidated in the future.
		- For `SOT666` there are elements duplicated on "Mechanical 18" and "Mechanical 255"! In Notecarrier-A, similar elements are duplicated on the Assembly and Silkscreen layers! Yet, shockingly, the footprint that actually appears on the board is different again (eg. the pin 1 dot is *inside* the outline).
			- Keeping true to the strategy of favouring equivalence in manufactured layers over everything else, and adopting the new conventions for `J-NANOSIM-SF72S006VBA` I will move the pin numbers to the `User.Comments` and move the outline off the Silkscreen on to the `F.Fab` layer.


### Layout

- Board origin is bottom *right*. This is super-confusing because the usual positive-up, positive-right convention remains. So the board has negative x ordinates and positive y ordinates. Yet the position file `PLACETOP.TXT` flips the x direction, so the ordinate value is the same, but the values are positive instead of negative.
	- Further, it seems the `PLACETOP.TXT` doesn't agree with the design file. Eg. `DS4` in `PLACETOP.TXT` is at `(62.8776, 18.7069)` and in the `brd` file is `(-62.8776, 16.3569)`. So the x-negation issue is corrected, but there's an unexplained y-offset.
		- While in `PLACEBOTTOM.TXT`, `J2` is at `(8.3184, 14.0875)` while in the design file it is at `(-67.9516, 14.0875)`. So now the x values don't agree.
		- In all, maybe a dozen of these descrepencies were found. It looks like at some point the connectors were all brought inboard (outboard for `J13` and `J14`) a millimeter or so (to the point the normal MicroUSB connector lip would foul with the edge of the board, so a "without flange style" variant must be used) and a few other components shifted to suit.
	- To very carefully minimise confusion as much as possible I'm going to **retain** the unusual origin, treat the `PLACETOP.TXT`/`PLACEBOTTOM.TXT` files with suspicion (since at least the design files are internally consistent, and they look correct compared to the physical sample I have) and deal with whatever results from that.
- An A3 sheet is unnecessary, so I'm sticking with A4. That makes a neat KiCad origin at `(130,140)`.
	- Therefore to place parts, I opened the `PLACETOP.TXT` file in a spreadsheet program, added a KiCad X column as `130-X` and a KiCad Y column as `140-Y` (since the X coordinate is inverted because the strange negative/positive convention mentioned above, and the Y coordinate is inverted in KiCad).
	- Then added a column like `"place[""" & TRIM($A2) & """] = (" & B2 & "," & C2 & "," & D2 & ");"` to produce Python code that will create a dict entry for every component.
	- And then type `place = {};` into `pcbnew` console, copy-paste the Python code column (might need to put it all on one line first), and finally, ran a script like this (then close and re-open PCB to refresh properly):

```
for p in pcb.GetFootprints():
    if p.GetReference() in place:
        (x,y,r) = place[p.GetReference()]
        p.SetPosition(pcbnew.VECTOR2I(pcbnew.wxPoint(x*1000000,y*1000000)))
        p.SetOrientationDegrees(r)
```

- Back side and mechanical only footprints can have their positions set by hand.
- Layers were imported as DXF as in Notecarrier-B, except this is a 4 layer board so the `GND` and `POWER` layers were imported to layers `User.8` and `User.9` respectively. The `VIA` layers they displaced were imported using the drill file technique described in Notecarrier-F instead.


### 3D

## Library

## Validation Method

## Produce Outputs



---

## References
