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

## PCB

## 3D

## Library

## Validation Method

## Produce Outputs



---

## References
