### 上层Taphanler拦截

```js
 gesturePolicy: TapHandler.ReleaseWithinBounds | TapHandler.WithinBounds
 grabPermissions: PointerHandler.CanTakeOverFromAnything 
			| PointerHandler.CanTakeOverFromHandlersOfSameType 
			| PointerHandler.CanTakeOverFromItems
            | PointHandler.ApprovesTakeOverByAnything 
			| PointHandler.ApprovesCancellation
```

