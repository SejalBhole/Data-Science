# Excel Practice: Car Parking Charges Using Nested IF

## Overview

This practice exercise demonstrates how to use **nested IF statements in Microsoft Excel** to calculate parking charges based on the number of hours a car is parked.

The exercise was completed using a parking dataset containing car registration numbers, hours parked, and calculated parking charges.

## Objective

Calculate the parking charge for each car according to different parking-duration thresholds and display **"Free Parking"** when the parking duration is below the minimum threshold.

## Excel Concepts Practiced

- Nested `IF` statements
- Absolute cell references
- Conditional logic
- Basic calculations
- Currency formatting
- Copying formulas down a column
- Using input cells for thresholds and fees

## Business Rules Used

The worksheet uses the following configurable values:

| Parameter | Cell | Value |
|---|---|---:|
| Threshold 1 | F7 | 6 hours |
| Threshold 2 | F8 | 3 hours |
| Long Hour Fee | F9 | £2.00/hour |
| Medium Hour Fee | F10 | £3.00/hour |

The logic is:

- If hours parked are **greater than 6**, charge `£2 × hours`.
- If hours parked are **greater than 3**, charge `£3 × hours`.
- Otherwise, display **"Free Parking"**.

## Formula Used

The formula entered in `C4` was:

```excel
=IF(B4>$F$7,$F$9*B4,IF(B4>$F$8,$F$10*B4,"Free Parking"))
```

The `$` signs make the threshold and fee cells **absolute references**, so the references remain fixed when the formula is copied down to the other rows.

## Example Results

| Car Registration | Hours Parked | Parking Charge |
|---|---:|---:|
| DA12 NEJ | 6 | £18.00 |
| MA16 BVW | 12 | £24.00 |
| DD11 SFD | 8 | £16.00 |
| MA14 NHG | 11 | £22.00 |
| YK14 BHH | 5 | £15.00 |
| DY15 FLB | 3 | Free Parking |
| MM12 SWL | 12 | £24.00 |
| MA16 GKW | 7 | £14.00 |
| FS12 DSD | 1 | Free Parking |
| DA11 SBM | 6 | £18.00 |

## Key Learning

This exercise helped practice how Excel can apply **multiple conditions sequentially** using nested `IF` statements.

It also demonstrated why **absolute references** are useful when a formula depends on fixed assumptions such as thresholds and pricing rates. Instead of hard-coding the values directly into the formula, the thresholds and fees were stored in separate cells, making the calculation easier to update.

## Skills Demonstrated

**Excel | Nested IF | Absolute References | Conditional Logic | Formulae | Data Analysis | Data Validation | Basic Business Rules**

## Interview Explanation

> "I practiced a parking-charge calculation in Excel where the charge depended on the number of hours parked. I used a nested IF formula with absolute references to separate threshold and fee values. This allowed me to apply multiple conditions and copy the formula across the dataset without changing the reference cells. The exercise helped me understand practical conditional logic and how to build flexible Excel calculations."

