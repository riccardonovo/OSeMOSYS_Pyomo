# Open Source energy MOdeling SYStem

##  Main changes to previous version OSeMOSYS_2020_11_13
- Inserted a scenario configurator section for defining SETS and PARAMETERS through excel workbooks
- Inserted a Functions section that contains the OSeMOSYS code (as a function) and a function for converting input data from excel workbook to .dat
- Fixed a bug in the storage equations that missed the product with DaisInDayType parameter in the StorageLevelDayTypeStart_rule
- Added the new Dispatchable Generation equations
- Modified the README

##  Main changes to previous version OSeMOSYS_2013_05_10

- Removed the parameter TechWithCapacityNeededToMeetPeakTS from constraint CAa4_Constraint_Capacity
- Fixed a bug related to using CapacityOfOneTechnologyUnit in constraint CAa5_TotalNewCapacity
- Fixed a bug in the storage equations which caused an error if more than one day type was used
- DiscountRate is no longer technology-specific. Therefore, DiscountRateStorage is now replaced by DiscountRate
