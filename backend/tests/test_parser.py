def test_parse_bfl():
    from app.services.parser import parse_bfl_file
    import os
    sample = "data/sample.bfl"
    if os.path.exists(sample):
        data = parse_bfl_file(sample)
        assert len(data) > 0
        assert "ax" in data[0]
    else:
        print("Sample .bfl not found — skipping")