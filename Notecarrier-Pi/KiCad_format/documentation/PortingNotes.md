# Porting Notes

As per [Notecarrier-A](../../../Notecarrier-B/KiCad_format/documentation/PortingNotes.md), except:

## Project

Nothing to report.

## Schematic

### Capture

Nothing to report.

### BOM

Nothing to report.

## PCB

### Footprints

- The `FORO-0270-U` footprint (2.7mm mounting hole) has a round via keepout and same size route keepout. In KiCad you would do this with a single rule area, but they don't support curves. So I've approximated it with a polygon.
	- This feature could be backported to `FORO-0330-U`, but that footprint has far less complexity. So the current port which uses the pad's clearance to provide "all" keepout is a worthy approximation, particularly since this seems to be how fills are behaving anyway.
	- The route keepout is violated on the board anyway by the `V+` track on the `In2.Cu` layer. I've chosen to port faithfully, and add the violation to the list of exclusions.
	- And even the clearance is different in practice! The footprint has a 4.4mm "antipad", but the fill on the `GND` layer has a 3.8mm clearance. In keeping with conventions established in this port, I've opted to duplicate the footprint, and apply the effective clearance to it. That way the PCB remains in perfect synchronicity with the schematic, and we still don't lose any information.
	- The footprint also has a "FILMMASK" layer for no obvious purpose. I've ported it to the `Adhesive` layers to retain the information, although note this results in a funny 3D view. See the 3D section below for details.
- I've changed my mind on the `J-5-0065-FOS-USB10118192-NOF` footprint. In Notecarrier-A I opted to reuse the `J-5-0065-FOS-MICROUSB10118192` footprint, since the only difference I could find was the 3D model. KiCad can handle multiple models within the same footprint, so in Notecarrier-A I just used the same footprint with a different model made visible. The same is true in Notecarrier-Pi, but it does create a DRC warning that the footprint does not match the one in the library, and running "update footprints from library" will override it with the version that has the original model visible.
	- Since this is the only DRC violation and the only reason why you can't update the PCB from the schematic, I've opted to create a separate footprint. I will back port it to Notecarrier-A too.


### Layout

- Another bottom-right origin, so will stick with same (130,140) origin in KiCad as in Notecarrier-A.
- To create the layout, the same techniques as described in the other ports was used. A good order of operations to reduce redundant work and context switching, is:
	1. Export all the OrCAD DXFs.
	1. Create the drill report.
	1. Check a couple of components in the `PLACETOP.TXT` and `PLACEBOTTOM.TXT` files in the gerbers archive against the PCB in OrCAD, to make sure they make sense. If not, reproduce the files.
	1. Assign footprints in KiCad schematic field editor.
	1. Flip two-terminal components in the schematic to ensure pin orientation matches original.
	1. Import the DXFs in each of the `User.` layers.
	1. Copy `User.1` items to `Edge.Cuts`.
	1. Update PCB from Schematic.
	1. Place components according to `PLACE` files.
	1. Place mounting holes manually.
	1. Check with `User.2` and `User.3` layers.
	1. Copy `User.4` items to `F.Silkscreen`. Copy the `User.5` items to `B.Silkscreen`.
	1. Position and size items on each silkscreen layer by importing the corresponding gerber into `User.Eco1` (via Gerber Viewer) and using it as a guide.
	1. Create tracks and zones for `F.Cu`, then `B.Cu` then `In1.Cu` and then `In2.Cu`, using the items in `User.6`, `User.7`, `User.8`, `User.9` respectively.
	1. Create vias from drill report.
- Oh no, the location of `J5` (the NanoSIM) is wrong in `PLACEBOTTOM.txt`. Lots of others are right though, so will just correct the descrepencies by hand.
	- The footprint has a different origin anyway!
	- `J4` (the MicroUSB) is also in the wrong place. Similar story to Notecarrier-A?
		- And `TVS1`, `C2`, `DS1`, `DS2`, `TVS3` and a bunch of others. Oh dear.
- The `In1.Cu` zone has a pull back from the board edge of 1mm. Unfortunately, the pull back from the slot is less than that! KiCad treats the slot the same as the board edge, so setting a global edge clearance wont work. Rather than defining an explicit zone edge that runs 1mm inside the outer board edge and having to deal with the curves somehow, I've opted to use the edge clearance setting as usual, and add a Custom Rule that disables it for the slot. I could have identified the slot using a different line width, but rather than confusing the manufacturer, I just used its rough location instead:

```
(rule DisableSlotPullBack
	(constraint edge_clearance (min 0mm))
	(condition "A.Type == 'Zone' && B.Start_X > 108mm && B.Start_X < 112mm && B.Start_Y > 119mm && B.Start_Y < 138mm"))
```

- On the other hand I did explicitly define the useless cutouts around 3 of the 4 mounting holes, for simplicity.
- To get the contradictory and seemingly arbitrary clearances around the NanoSIM, I did something similar to NoteCarrier-A - set zone clearance low and created tightly scoped custom rules, like:

```
(rule GndZone2GndPad
	(constraint physical_clearance (min 0.127mm))
	(condition "A.Type == 'Zone' && A.NetName == 'GND' && A.Name != 'SolidGND' && B.Type == 'Pad' && B.Pad_Type == 'SMD' && B.NetName == 'GND'"))
(rule Zone2Default
	(constraint clearance (min 0.3mm))
	(condition "A.Type == 'Zone' && (B.NetClass == 'Default' || B.NetName == '')"))
(rule Zone2SIM_CLK
	(constraint clearance (min 0.15mm))
	(condition "A.Type == 'Zone' && (B.Type == 'Pad' && B.NetName == '/SIM_CLK')"))
(rule Zone2J2-CLK
	(constraint clearance (min 0.3mm))
	(condition "A.Type == 'Zone' && B.NetClass == 'J2-CLK'"))
(rule NanoSIMZone2J2-CLK
	(layer "B.Cu")
	(constraint clearance (min 0.15mm))
	(condition "A.Type == 'Zone' && B.NetClass == 'J2-CLK'"))
```

- The minimum clearance is specified as 0.2mm, but the track on pad 5 of `TVS4` is only 0.198mm away from pad 4. This is trivial mistake, so I've ported the rule faithfully and just let the violation stand.
- As in Notecarrier-A, I have not captured these manufacturing instructions anywhere, so will list them here in case they are important:
		- CTI: 175V
		- E-Testing: Yes
		- UL-Marking: Yes
		- Board tolerance (X|Y|Z): ±0.2|±0.2|±10%

### 3D

- The adhesive layer in the `FORO-0270-U` footprint, which is a port of the strange "FILMMASK" layer in the original, causes the mounting holes to fill with purple (front) and blue (back). This looks a bit funny, but has no material impact.


## Validation

As per Notecarrier-A.

- No testpoints so testpoint report not generated.
- The gerber diff method uses the board outline / edge cuts layer to align and match size between OrCAD and KiCad gerbers. In this case, that means the slot cutout appears in the KiCad pngs but not the OrCAD one (which uses a NCROUTE_PATH element for the slot). So all diffs will show a green slot cutout. This can safely be ignored.
	- The slot itself is validated in the PTH gerber diff.
- The DXF export necked tracks from 0.3mm to 0.25mm and 0.2mm at the wrong segment. Both the design files and the gerber archive agree this is wrong. Odd, but no rhyme or reason apparent, and easy to spot in the diffs, so I've just corrected them manually.

