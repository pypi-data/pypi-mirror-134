import { expect } from 'chai'

import { Rectangle } from '../src/index'

describe("Rectangle", () => {
    if("should have width and height", () => {
        const rect = new Rectangle(100, 100)
        expect(rect.width).equal(100)
        expect(rect.height).equal(100)
    });
});

