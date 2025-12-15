# MVC Architecture - Sheet2DB Project

## Overview
This document explains the Model-View-Controller (MVC) architecture implementation in the Sheet2DB project.

## Architecture Diagram

```
┌─────────────────────────────────────────────────────────────┐
│                          main.py                            │
│                    (Application Entry)                      │
└──────────────────────┬──────────────────────────────────────┘
                       │
                       ▼
┌─────────────────────────────────────────────────────────────┐
│                    CONTROLLER                               │
│              (pipeline_controller.py)                       │
│                                                             │
│  • Orchestrates application flow                           │
│  • Handles user actions                                    │
│  • Validates business logic                                │
│  • Coordinates Model ↔ View                                │
└──────────────┬─────────────────────────┬────────────────────┘
               │                         │
      ┌────────▼────────┐       ┌───────▼────────┐
      │     MODEL       │       │      VIEW      │
      │   (model/)      │       │    (view/)     │
      │                 │       │                │
      │ • CSVReader     │       │ • WebUI        │
      │ • ExcelReader   │       │ • Components   │
      │ • Validator     │       │                │
      │ • PostgresLoader│       │ Display only   │
      │                 │       │ No logic       │
      │ Business logic  │       └────────────────┘
      │ Data processing │
      └─────────────────┘
```

## Responsibilities

### 🎮 CONTROLLER (pipeline_controller.py)
**Role:** Orchestrator and decision maker

#### What it SHOULD do:
- ✅ Handle user actions and events
- ✅ Validate business logic
- ✅ Coordinate between Model and View
- ✅ Process form submissions
- ✅ Handle errors and exceptions
- ✅ Make decisions based on data
- ✅ Control application flow

#### What it SHOULD NOT do:
- ❌ Display UI elements
- ❌ Read/write files directly
- ❌ Contain HTML/CSS/styling
- ❌ Query database directly

#### Example Flow:
```python
def _insert_flow(self):
    # 1. Get data from View
    expense_data = self.view.get_insert_form_data()
    
    # 2. Process (Controller's job)
    if expense_data and expense_data.get("submitted"):
        df = pd.DataFrame([expense_data])
        
        # 3. Use Model to validate
        validated_df = self.validator.validate(df)
        
        # 4. Use Model to save
        self.loader.load_data(validated_df)
        
        # 5. Update View with result
        self.view.show_success("Saved!")
```

### 🎨 VIEW (web_ui.py + components/)
**Role:** Pure presentation layer

#### What it SHOULD do:
- ✅ Display UI elements
- ✅ Capture user input
- ✅ Return data to controller
- ✅ Show feedback messages
- ✅ Format data for display
- ✅ Handle UI state (tabs, forms)

#### What it SHOULD NOT do:
- ❌ Validate data
- ❌ Process business logic
- ❌ Call database directly
- ❌ Read files
- ❌ Make business decisions

#### Example Component:
```python
class InsertComponent:
    def render(self) -> Dict[str, Any]:
        """Just display form and return data"""
        with st.form("form"):
            date = st.date_input("Date")
            amount = st.number_input("Amount")
            submit = st.form_submit_button("Submit")
        
        # Return structured data
        return {
            "date": date,
            "amount": amount,
            "submitted": submit
        }
```

### 📦 MODEL (model/)
**Role:** Data and business logic

#### What it SHOULD do:
- ✅ Read/write data (CSV, Excel, DB)
- ✅ Validate data schemas
- ✅ Transform data
- ✅ Apply business rules
- ✅ Query database
- ✅ Data processing

#### What it SHOULD NOT do:
- ❌ Display UI elements
- ❌ Know about Streamlit
- ❌ Handle user events
- ❌ Show error messages

#### Example:
```python
class CSVReader(Reader):
    def read_data(self, file: str) -> pd.DataFrame:
        """Pure data reading - no UI"""
        return pd.read_csv(file, **self.config)
```

## Communication Flow

### 1. User Action Flow
```
User clicks button
    ↓
View captures click → returns data to Controller
    ↓
Controller validates → calls Model
    ↓
Model processes → returns result
    ↓
Controller decides → tells View what to show
    ↓
View displays result
```

### 2. Data Flow Example: Insert Expense
```
1. User fills form in InsertComponent
2. View returns {date, description, amount, submitted: true}
3. Controller receives data
4. Controller creates DataFrame
5. Controller calls validator.validate(df)
6. Controller calls loader.load_data(df)
7. Controller tells View to show success message
```

## Key Improvements Made

### ❌ BEFORE (Wrong Pattern)
```python
# Controller was just a passthrough
def _insert_flow(self):
    date, desc, cat, amt, btn = self.view.show_insert()
    # Nothing happens! No processing!

# View was returning raw values
def render(self):
    return (date, desc, cat, amt, btn)  # Tuple? Hard to use!
```

### ✅ AFTER (Correct Pattern)
```python
# Controller actually controls
def _insert_flow(self):
    data = self.view.get_insert_form_data()
    if data["submitted"]:
        df = self._create_dataframe(data)
        validated_df = self.validator.validate(df)
        self.loader.load_data(validated_df)
        self.view.show_success("Saved!")

# View returns structured data
def render(self) -> Dict[str, Any]:
    return {"date": date, "amount": amt, "submitted": btn}
```

## Common MVC Mistakes to Avoid

### ❌ Mistake 1: Business Logic in View
```python
# WRONG - View should not validate
class InsertComponent:
    def render(self):
        amount = st.number_input("Amount")
        if amount < 0:  # ❌ Validation in View!
            st.error("Must be positive")
```

### ✅ Correct: Validation in Controller/Model
```python
# RIGHT - Validation in Controller
def _insert_flow(self):
    data = self.view.get_insert_form_data()
    if data["amount"] < 0:  # ✅ Validation in Controller
        self.view.show_error("Must be positive")
```

### ❌ Mistake 2: UI in Controller
```python
# WRONG - Controller should not use st.write
def _insert_flow(self):
    st.write("Processing...")  # ❌ UI in Controller!
    self.process_data()
```

### ✅ Correct: UI through View
```python
# RIGHT - Controller tells View what to show
def _insert_flow(self):
    self.view.show_info("Processing...")  # ✅ Through View
    self.process_data()
```

### ❌ Mistake 3: Data Processing in View
```python
# WRONG - View should not transform data
class ViewComponent:
    def render(self, df):
        df = df.groupby("category").sum()  # ❌ Processing in View!
        st.dataframe(df)
```

### ✅ Correct: Processing in Controller/Model
```python
# RIGHT - Controller processes, View displays
def _view_flow(self):
    df = self._fetch_data()
    aggregated = df.groupby("category").sum()  # ✅ In Controller
    self.view.show_data_view(aggregated)
```

## Testing Benefits of Good MVC

### Easy to Test Controller
```python
def test_insert_flow():
    mock_view = Mock()
    mock_view.get_insert_form_data.return_value = {
        "date": "2024-01-01",
        "amount": 100,
        "submitted": True
    }
    
    controller = PipelineController(mock_view)
    controller._insert_flow()
    
    mock_view.show_success.assert_called_once()
```

### Easy to Test Model
```python
def test_csv_reader():
    reader = CSVReader()
    df = reader.read_data("test.csv")
    assert len(df) > 0
```

### Easy to Test View
```python
def test_insert_component():
    component = InsertComponent()
    result = component.render()
    assert "date" in result
    assert "amount" in result
```

## Best Practices

1. **Controller decides, View displays**
2. **Model knows nothing about UI**
3. **View returns data as dictionaries, not tuples**
4. **Use type hints for clarity**
5. **Keep components single-purpose**
6. **Add docstrings explaining responsibilities**
7. **Separate concerns strictly**

## Quick Reference

| Layer      | Can Access | Cannot Access |
|------------|-----------|---------------|
| View       | Streamlit, Components | Model, Database |
| Controller | View, Model | Direct DB, Direct File I/O |
| Model      | Database, Files | Streamlit, View |

---

**Remember:** When in doubt, ask: "Who should know about this?"
- UI? → View
- Business rules? → Controller/Model
- Data operations? → Model
