# flake8: noqa: E402
import pandas as pd
from io import StringIO
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parent.parent / "src"))  # noqa: E402
from process_books import main

def test_process_books(monkeypatch, tmp_path):
    # Create a mock CSV in a temporary directory
    csv_content = """Title,Category,Author
Book1,Fiction,AuthorA
Book2,Science,AuthorB
Book3,Fiction,AuthorC
Book4,History,AuthorD
Book5,Science,AuthorE
"""
    data_dir = tmp_path / "data"
    data_dir.mkdir()
    csv_file = data_dir / "Books_Dataset.csv"
    csv_file.write_text(csv_content)

    # Patch the path used in process_books.py to point to our temp CSV
    monkeypatch.setattr(
        "process_books.pd.read_csv", lambda path: pd.read_csv(csv_file)
    )

    # Capture stdout
    captured_output = StringIO()
    sys.stdout = captured_output

    main()

    sys.stdout = sys.__stdout__
    output = captured_output.getvalue()

    # Basic assertions
    assert "Book counts by category" in output
    assert "Fiction" in output
    assert "Science" in output
    assert "History" in output
    assert "First 5 books" in output
    assert "Book1" in output
    assert "Book5" in output
