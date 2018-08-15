# Most Recent Updates:
- Segmented code a little bit more. Now there is one method that plots the On-Edge Control, Notch, and Seam attacks (all in the same .MAT file). A separate method will plot the support material attack against the On-Edge Control. Yet another method will plot the Density change attack against the Flat Control. A final method plots the temperature attack specimens all overlaid for visual clarity.

# Bug Fixes:
- Fixed the first three plots being "control specimen" by moving reset_output after "show"
- Fixed the error from the show on plots 4 and 5 by setting to a static line color (problem with indexing)

# To Do:
- Overlay Control specimen data on each attack test (make it see through, different color, and wider than the attack specimen data)
- Remove the outliers in the second plot
- Separate out the Density Change attack and plot its control specimen data on top of it
- Overlay Attacks 2-4 on top of each other
- Support material attacks are in Batch_1.mat, Batch_2.mat, and Batch_3.mat. What do XZF, XZS, and XZS_BigGap mean?
