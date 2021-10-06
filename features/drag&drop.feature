Feature: Drag & Drop

Scenario: Drag & drop element to target
  Given user is in url page https://qavbox.github.io/demo/dragndrop/
  And two boxes appeared
  When user select "Drag" Box
  And Drop it to "Drop here" box
  Then Dropped text appears
