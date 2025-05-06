# tests/test_log.py

import pytest
from corstream import Stream


@pytest.mark.asyncio
async def test_log_passthrough(capsys):
    result = []
    
    await (
        Stream
        .from_iterable([10, 20])
        .log()
        .for_each(lambda x: result.append(x))
    )
    
    assert result == [10, 20]
    
    captured = capsys.readouterr()
    assert "10" in captured.out
    assert "20" in captured.out
    
@pytest.mark.asyncio
async def test_log_with_label(capsys):
    result = []
    
    await (
        Stream
        .from_iterable(["a", "b"])
        .log(label="debug")
        .for_each(lambda x: result.append(x))
    )
    
    assert result == ["a", "b"]
    
    captured = capsys.readouterr()
    assert "[debug] a" in captured.out
    assert "[debug] b" in captured.out