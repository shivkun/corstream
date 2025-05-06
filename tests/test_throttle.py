# tests/test_throttle.py

import pytest
import time
from corstream import Stream


@pytest.mark.asyncio
async def test_throttle_respects_timing():
    timestamps = []
    
    async def record_timestamp(x):
        timestamps.append(time.perf_counter())
        
    start = time.perf_counter()
    
    await (
        Stream
        .from_iterable([1, 2, 3])
        .throttle(rate=1, per_seconds=0.1)
        .for_each(record_timestamp)
    )
    
    assert len(timestamps) == 3
    diffs = [timestamps[i+1] - timestamps[i] for i in range(len(timestamps) - 1)]
    for d in diffs:
        assert 0.08 <= d <= 0.2 # Account for async jitter
        
    total_duration = timestamps[-1] - start
    assert total_duration >= 0.2
    
@pytest.mark.asyncio
async def test_throttle_invalid_arguments():
    with pytest.raises(ValueError):
        Stream.from_iterable([1]).throttle(rate=0, per_seconds=1)
        
    with pytest.raises(ValueError):
        Stream.from_iterable([1]).throttle(rate=1, per_seconds=0)