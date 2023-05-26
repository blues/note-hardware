# Porting Notes

As per [Notecarrier-A](../../../Notecarrier-B/KiCad_format/documentation/PortingNotes.md), except:

## Project

## Schematic

### BOM


## PCB

### Footprints

- The `FORO-0270-U` footprint (2.7mm mounting hole) has a round via keepout and same size route keepout. In KiCad you would do this with a single rule area, but they don't support curves. So I've approximated it with a polygon.
	- This feature could be backported to `FORO-0330-U`, but that footprint has far less complexity. So the current port which uses the pad's clearance to provide "all" keepout is a worthy approximation, particularly since this seems to be how fills are behaving anyway.

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


### 3D

## Validation

---

## References

# TODO
